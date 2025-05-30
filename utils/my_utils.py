import numpy as np
import tensorflow as tf
import pickle
from scipy.special import erfc


def ebno_db_setup(Ps_dBm, No_dBm_per_Hz, B_Hz, R):
    Pn_dBm = No_dBm_per_Hz + 10 * np.log10(B_Hz)

    # Calculate SNR in dB
    SNR_dB = Ps_dBm - Pn_dBm

    # Calculate Eb/N0 in dB
    EbNo_dB = SNR_dB - 10 * np.log10(R)

    return EbNo_dB


def bit2onehot(bits,m, batch_size,num_symbols_per_codeword):
    bits_vector = tf.reshape(bits, [-1, m])

    indices = tf.reduce_sum(bits_vector * (2 ** tf.range(m - 1, -1, -1, dtype=tf.float32)), axis=-1)
    one_hot = tf.one_hot(tf.cast(indices, tf.int32), depth=2**m, dtype=tf.float32)
    one_hot = tf.reshape(one_hot,[batch_size,num_symbols_per_codeword, 2**m])

    return bits_vector, indices, one_hot



def indices_to_bits(indices, num_bits_per_symbol, batch_size):
    bit_positions = tf.cast(tf.range(num_bits_per_symbol - 1, -1, -1), dtype=indices.dtype)
    bit_matrix = tf.bitwise.right_shift(
        tf.expand_dims(indices, axis=-1),
        bit_positions
    ) & 1

    code_length = tf.shape(indices)[1] * num_bits_per_symbol
    bit_streams = tf.reshape(bit_matrix, [batch_size, code_length])

    return bit_matrix, bit_streams

def Normalize(x):

    total_energy = tf.reduce_sum(tf.abs(x)**2)
    num_elements = tf.cast(tf.size(x), tf.float32)
    avg_power = total_energy / num_elements

    epsilon = 1e-12
    norm_factor = tf.sqrt(tf.maximum(avg_power, epsilon))

    norm_factor = tf.complex(norm_factor, tf.constant(0.0))
    x_normalized = x / norm_factor

    return x_normalized


def one_hot_Mqam(M):
    symbols = tf.range(M, dtype=tf.int32)
    one_hot = tf.one_hot(symbols, depth=M)
    return tf.cast(one_hot, tf.float32)




def load_weights(model, model_weights_path):
    model(tf.constant(1, tf.int32), tf.constant(7.0, tf.float32))
    with open(model_weights_path, 'rb') as f:
        weights = pickle.load(f)
    model.set_weights(weights)

def save_weights(model, model_weights_path):
    weights = model.get_weights()
    with open(model_weights_path, 'wb') as f:
        pickle.dump(weights, f)


def Q_func(x):
    return 0.5 * erfc(x / np.sqrt(2))