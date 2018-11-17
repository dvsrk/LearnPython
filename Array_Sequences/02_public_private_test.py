class M(object):

    def public(self):
        print 'You can use tab to see me'

    # methods declared / started with underscore can't be viewed by default.
    def _private(self):
        print 'You can''t see me with tab'

obj = M()
obj.public()
obj._private()
