import re
import game
import wiki

lead = game.Guy("Team Lead")
colleague = game.Guy("Peter")

lead.say(
    "Welcome to your new job! I am your team lead and I will show you how we "
    "work here. It may take some time to learn how to use our tools, but I'm "
    "sure you'll get the hang of it in no time."
)

lead.say(
    "First you will have to set up a password for your work machine. Company "
    "policy says it needs to pass some minimum requirements. Number, letters, "
    "length, you know, the usual. Type in 'set_my_password' followed your new "
    "password."
)

log = []

class Rule:
    def __init__(
        self, pattern, message, condition=lambda: True, action=lambda: None
    ):
        self.pattern = pattern
        self.message = message
        self.condition = condition
        self.action = action

variables = {}

rules = [
    Rule("set_my_password .{0,5}", "Password must have at least length 6."),
    Rule("set_my_password [^\\d]+", "Password must contain a number."),
    Rule(
        "set_my_password [^a-z]+", "Password must contain a lower case letter."
    ),
    Rule(
        "set_my_password [^A-Z]+", 
        "Password must contain an upper case letter."
    ),
    Rule(
        "set_my_password .+", "Error 528.", 
        lambda: "illegal_letter" not in variables,
        lambda: (
            variables.update(illegal_letter=log[-1][-3].lower()), 
            lead.say(
                "Oh, right. There is an issue where some symbols don't work. "
                "Was it '" + log[-1][-4] + "'? Just try some."
            )
        )
    ),
    Rule(
        "set_my_password .+", "Error 528.", 
        lambda: variables["illegal_letter"] in log[-1][16:].lower()
    ),
    Rule(
        "set_my_password .+", "Password updated.", 
        action=lambda: (
            variables.update(password=log[-1][16:]),
            lead.say(
                "Good. Now you can use your work computer. There are a few "
                "useful commands you should keep in mind. Take notes!"
            ),
            lead.say(
                "'wiki' followed by a search term lets you search through our "
                "documentation. Use it whenever you are stuck!"
            ),
            lead.say(
                "'lit' is our version control solution. Use 'lit switch' "
                "followed by a version number to download that versions of "
                "our project. Use 'lit push' to upload your changes to "
                "our server. "
            ),
            lead.say(
                "Your computer comes pre-installed with 'bscode' to edit "
                "files."
            ),
        )
    ),
    Rule(
        ".+", "Account locked. Set password.", 
        lambda: "password" not in variables
    ),
    Rule(
        "wiki \\S+", None, action=lambda: wiki.search(log[-1][5:])
    ),
]

while True:
    log.append(input("\t> "))

    for rule in rules:
        if re.fullmatch(rule.pattern, log[-1]) and rule.condition():
            if rule.message:
                game.write(rule.message)
            rule.action()
            break
