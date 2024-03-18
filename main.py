import json

from linkedin_api import Linkedin

linkedin = Linkedin("vanen31@gmail.com", "JavaDev2023!")

profile = linkedin.get_profile("ivan-fedotov-54677a1a1")
profile["contact_info"] = linkedin.get_profile_contact_info(
    "ivan-fedotov-54677a1a1"
)
connections = linkedin.get_profile_connections(profile["profile_id"])
# send a message
# linkedin.send_message(
#     recipients=[profile["profile_id"]],
#     message="Hello, Hola, Namaste, Hii, Bonjour, Guten Tag",
# )
