import tensorflow as tf

print(tf.config.list_physical_devices('GPU'))  # if an empty list is returned than GPU access is not available
