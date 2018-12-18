"""z2_color implementation with batch normalization."""
from keras.models import Model
from keras.layers import Input, BatchNormalization, AveragePooling2D, Conv2D, \
                         MaxPooling2D, Dense, ZeroPadding2D, Flatten, concatenate
from keras import optimizers
from keras import regularizers
from keras.layers.core import Lambda, Dropout, Reshape
from keras.layers import Activation, merge
from keras import backend as K
from keras.engine import Layer, InputSpec
from keras import initializers, regularizers, constraints
from Net import Net
import numpy as np

    
class NvidiaNet(Net):
    def __init__(self, meta_label=6, input_width=672, input_height=376):
        super(NvidiaNet, self).__init__(meta_label, input_width, input_height)
        self.metadata_size = (11, 20)
    
    def _get_model(self):
        ZED_data = Input(shape=(self.input_height, self.input_width, self.N_CHANNEL*4), name='ZED_input')
        metadata = Input(shape=(self.meta_label, 11, 20), name='meta_input')
        conv1 = Conv2D(filters=24, kernel_size=5, activation='relu', strides=(2,2))(ZED_data)
        conv2 = Conv2D(filters=36, kernel_size=5, activation='relu', strides=(2,2))(conv1)
        conv3 = Conv2D(filters=48, kernel_size=5, activation='relu', strides=(2,2))(conv2)
        conv4 = Conv2D(filters=64, kernel_size=3, activation='relu')(conv3)
        conv5 = Conv2D(filters=64, kernel_size=3, activation='relu')(conv4)
        drop1 = Dropout(rate=0.7, name='drop1')(conv5)
        flat = Flatten()(drop1)
        dense1 = Dense(units=100)(flat)
        dense2 = Dense(units=50)(dense1)
        out = Dense(units=20, name='out')(dense2)
        
        model = Model(inputs=[ZED_data, metadata], outputs=out)
        return model
    
    def get_layer_output(self, model_input, training_flag = True):
        get_outputs = K.function([self.net.layers[0].input, K.learning_phase()],
                                 [self.net.layers[10].output])
        layer_outputs = get_outputs([model_input['ZED_input'], training_flag])[0]
        return layer_outputs 


def unit_test():
    test_net = NvidiaNet(6, 672, 376)
    test_net.model_init()
    test_net.net.summary()
    a = test_net.forward({'ZED_input': np.random.rand(1, 376, 672, 12),
                          'meta_input': np.random.rand(1, 6, 11, 20)})
    
    print(a)


unit_test()
