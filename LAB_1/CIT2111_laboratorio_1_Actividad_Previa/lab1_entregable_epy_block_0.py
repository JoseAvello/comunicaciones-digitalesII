import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Muestreo Instantaneo Plano',
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )

    def work(self, input_items, output_items):
        in_data = input_items[0]
        in_ctrl = input_items[1]
        out = output_items[0]

        for i in range(len(out)):
                    is_high = in_ctrl[i] > 0

                    if is_high and not self.was_high:
                        self.held_value = in_data[i]

                    if is_high:
                        out[i] = self.held_value
                        
                    else:
                        out[i] = 0.0

                    self.was_high = is_high

        return len(out)
