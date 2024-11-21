import game

wiki = [
    "Home: Software Corp., founded in 1978, is market leader in high-quality "
    "light frobnication.",

    "Maintenance Periods: Please note that every Monday between 1 and 2 pm "
    "our lit servers are taken down for maintenance. There may be additional "
    "down times.",

    "Common Configuration: The frobnication service configuration is split up "
    "into three main files, in order of precedence: "
    "'user/config.ini', 'config.ini' and 'base/super.yaml'.",

    "Compatibility Notice: To build versions earlier than 204.701.103 you "
    "need to pass '--legacy_mode' to 'cake' due to a compiler update.",

    "Version Numbers: We use 6 part version numbers "
    "'base.major.submajor_minor.lane.cycle'. E.g. '1.2.3_4.5.6'. "
    "Previously we had some parts combined to e.g. '0102.0304.0506'. You "
    "might see this format in older code.",

    "Parity Check: For security, the 'base/super.yaml' configuration goes "
    "through a parity check. It is only valid if it has an even number of 1 "
    "bits.",

    "Building The Project: We use the 'cake' command line utility. Simply run "
    "'cake configure' followed by 'cake build'. Run 'cake clean' to remove "
    "the built files again.",
]

def search(term):
    results = []
    for page in wiki:
        if page.find(term) != -1:
            results.append(page)
    game.write(str(len(results)) + " results.")
    if len(results) > 3:
        game.write("Showing first 3.")
    for result in results[:3]:
        game.write(result)
