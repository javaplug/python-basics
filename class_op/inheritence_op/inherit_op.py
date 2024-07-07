import class_op.inheritence_op.parent as p
import class_op.inheritence_op.child_new_method as c1
import class_op.inheritence_op.child_new_constructor as cc


p1 = p.Parent(21)
print('from Main P1')
p1.grok()

child1 = c1.ChildNewMethod(23)
print('from Main C1')
child1.grok()
child1.new_method()

child_constr = cc.ChildNewConstructor(21, 34)
print('from Main cc')
child_constr.grok()
child_constr.use_new_value()

