from requests import Session

class Rps101:
	def __init__(self) -> None:
		self.api = "https://rps101.pythonanywhere.com/api/v1"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
		}

	def _get(self, endpoint: str, params: dict = {}) -> dict:
		return self._get(
			f"{self.api}{endpoint}", params=params).json()

	def get_all_objects(self) -> dict:
		return self._get("/objects/all").json()

	def get_object_info(self, object_name: str) -> dict:
		return self._get(f"/objects/{object_name}").json()

	def get_match_result(
			self, object_one: str, object_two: str) -> dict:
		params = {
			"object_one": object_one,
			"object_two": object_two
		}
		return self._get("/match", params).json()
