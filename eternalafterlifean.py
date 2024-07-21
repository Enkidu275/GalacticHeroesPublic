#     *\___*
#   *^-/   \--_
#     _\___/-_/\___    _/
#    *    |   \_/_ \ _/         Eternal Afterlife, AN
#         *       \_|_          Copyright, Enheduana
#                _/ | \___/     Cycling Manifold Mind
#              _/    \
#                    /

# Iterates Through Neuron Array In Loop Endlessly
# Separate Processor Handles I/O. Carried Over At End of Neuron List.
# Input Affects Latent Charge. Emitted Signal Also Effects Output

# A neuron body contains (total 8 bytes)

# latent charge(1 byte): Environmental Input
# charge(1 byte): the combined signals and latent values received
# upper(1 byte): if charge is more than this, signal is the difference
# lower(1 byte): if charge is less than this, signal is the difference
# signal(1 byte): axon-emitted value to be received by another neuron's dendrite
# record of signal(1 byte): bits shift right, if neuron is signalling, first bit is set to 1
# repetitive signal(1 byte): if record of signal is 255 or 0, +1, else shift bits right
# repetitive punish(1 byte): if punish, +1, if reward, shift bits right

# A dendrite (charge receiver for neuron) contains

# signal pointer (4 bytes) 0 if empty. else, points to signal received from other neuron. (axon)
# threshhold (1 byte) if signal exceeds this value, difference is added to total charge of neuron body
# record of signal (1 byte) used to determine relationship for punishment inversion
