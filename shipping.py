class ShippingContainer:

    next_serial = 1337

    def _generate_serial(self):
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result


    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        # self.serial += self.next_serial += doesnt create a new instance variable
        ShippingContainer.next_serial += 1



#LEGB, class doesnt introduce scope in python
# Local  --> Inside the current fucntion
# Enclosing --> Inside Enclosing Functions
# Global --> At top level of the module
# Built-in --> In the special built in modules

class MyClass:

    b = "onclass"

    def __init__(self):
        self.a = "oninstance"

        print(self.a)

        print(MyClass.b)

        print(self.b) #--> access class attribute, since there is no instance attribute

        self.a = "re-bound" # --> rebinds the existing instance attribute 
        self.b  = "new on instance"  # --> instance attribute hides the class attribute, instance attribue takes precedence over class attribute

        print(self.b) # --> access the instance attribute







