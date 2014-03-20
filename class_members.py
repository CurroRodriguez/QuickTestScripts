'''
To test once and for all how can members be initialized.
'''


class ClassWithMembers(object):
    CONSTANT_MEMBER = 'CONSTANT_MEMBER'

    def __init__(self):
        self.construction_member = 'construction_member'


    def run(self):
        print 'Within a class method:'
        print 'self.CONSTANT_MEMBER = ' + self.CONSTANT_MEMBER
        print 'self.construction_member = ' + self.construction_member



obj = ClassWithMembers()
obj.run()
print 'Outside of class:'
print ClassWithMembers.CONSTANT_MEMBER 