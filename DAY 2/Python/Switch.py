# A switch statement is a multiway branch statement that compares the value of a variable to the values specified in case statements.
# function(argument){
#     switch(argument) {
#         case 0:
#             return "This is Case Zero";
#         case 1:
#             return " This is Case One";
#         case 2:
#             return " This is Case Two ";
#         default:
#             return "nothing";
#     };
# };


def switchExample(arg):
    switcher = {
        0: "Case Zero",
        1: "Case One",
        2: "Case Two",
    }
    return switcher.get(arg, "Nothing")


if __name__ == "__main__":
    arg = 1
    print(switchExample(arg))
