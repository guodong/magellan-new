import astunparse

from table import Table
from variable import RefVariable


class Instruction:
    def __init__(self, gv, inputs, outputs, mapping):
        self.gv = gv
        self.inputs = inputs
        self.outputs = outputs
        self.mapping = mapping
        self.pit = Table()

    def gen_pit(self):

        for output in self.outputs:
            self.pit.schema.outputs.append(output.name)

        if self.mapping == 'valof':
            self.pit.schema.inputs.append(self.inputs[1].name)
            for (k, v) in self.inputs[0].value.items():
                entry = {
                    self.inputs[1].name: k,
                    self.outputs[0].name: v
                }
                self.pit.entries.append(entry)
        elif self.mapping == 'in':
            self.pit.schema.inputs.append(self.inputs[0].name)
            v = self.inputs[1]
            if isinstance(self.inputs[1], RefVariable):
                v = self.inputs[1].dst
            for val in v.value.keys():
                entry = {
                    self.inputs[0].name: val,
                    self.outputs[0].name: 'True'
                }
                self.pit.entries.append(entry)
        else:
            for input in self.inputs:
                self.pit.schema.inputs.append(input.name)



    def dump(self):
        if self.gv is not None:
            if len(self.outputs) == 0:
                print 'if %s: %s(%s)' % (self.gv.name, self.mapping,
                                          ', '.join(map(lambda s: s.dump(), self.inputs)))
            else:
                print 'if %s: %s = %s(%s)' % (self.gv.name, ', '.join(map(lambda s: s.dump(), self.outputs)), self.mapping,
                                          ', '.join(map(lambda s: s.dump(), self.inputs)))
        else:
            if len(self.outputs) == 0:
                print '%s(%s)' % (self.mapping,
                                       ', '.join(map(lambda s: s.dump(), self.inputs)))
            else:
                print '%s = %s(%s)' % (', '.join(map(lambda s: s.dump(), self.outputs)), self.mapping,
                                   ', '.join(map(lambda s: s.dump(), self.inputs)))
        # s1 = ' '.join(map(lambda s: astunparse.unparse(s), self.outputs))
        # print '%s = func(%s)' % (s1, ' '.join(map(lambda s: astunparse.unparse(s), self.inputs)))
        # print '%s = assign(%s)' % (' '.join(map(lambda s: s.id, self.outputs)), ' '.join(map(lambda s: s.n, self.inputs)))

    def dump_pit(self):
        # if self.mapping == 'valof':

        gv = ''
        if self.gv is not None:
            gv = self.gv.name
            print '%s | %s -> %s' % (gv, '|'.join(self.pit.schema.inputs), '|'.join(self.pit.schema.outputs))
        else:
            print '%s -> %s' % ('|'.join(self.pit.schema.inputs), '|'.join(self.pit.schema.outputs))


        for entry in self.pit.entries:
            for input_name in self.pit.schema.inputs:
                print entry[input_name] + '|',
            for output_name in self.pit.schema.outputs:
                print entry[output_name] + '|'
