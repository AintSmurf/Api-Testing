from backend.src.utilities.requestsUtility import RequestsUtility


class Coupon_Helper():

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.endpoint = 'coupons'

    def create_coupon(self, payload):
        return self.requests_utility.post(endpoint=self.endpoint, payload=payload, expected_status_code=201)


    def get_all_copouns(self):
        return self.requests_utility.get(endpoint=self.endpoint)

    def delete_specefic_coupon_with_id(self,cp_id):
        return self.requests_utility.delete(endpoint=self.endpoint,id_num=cp_id)

    def update_coupon_percentage(self,cp_id, payload):
        return self.requests_utility.put(endpoint=self.endpoint,id_num=cp_id, payload=payload)
