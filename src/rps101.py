from requests import Session

class Rps101:
	def __init__(self) -> None:
		self.api = "https://rps101.pythonanywhere.com/api/v1"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
		}

	def get_all_objects(self) -> dict:
		return self.session.get(f"{self.api}/objects/all").json()

	def get_object_info(self, object_name: str) -> dict:
		return self.session.get(f"{self.api}/objects/{object_name}").json()

	def get_match_result(
			self, object_one: str, object_two: str) -> dict:
		return self.session.get(
			f"{self.api}/match?object_one={object_one}&object_two={object_two}").json()
