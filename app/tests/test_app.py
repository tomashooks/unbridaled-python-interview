from app.tests.base import BaseSetup


class TestApp(BaseSetup):
    @staticmethod
    def get_payload() -> dict:
        return {
            "name": "Standard-hilt lightsaber",
            "uom": "pcs",
            "category_name": "lightsaber",
            "is_producible": True,
            "is_purchasable": True,
            "type": "product",
            "purchase_uom": "pcs",
            "purchase_uom_conversion_rate": 0,
            "batch_tracked": True,
            "additional_info": "string",
            "variants": [
                {
                    "sku": "EM",
                    "sales_price": 40,
                    "purchase_price": 0,
                    "type": "product",
                    "config_attributes": [
                        {
                            "config_name": "Type",
                            "config_value": "Standard"
                        }
                    ]
                }
            ]
        }

    def test_create_product_default_uom(self):
        response = self.test_client.post(
            "/v1/products/create/",
            json=self.get_payload()
        )
        self.assertEqual(response.status_code, 200, response.json())
        response = self.test_client.post(
            "/v1/products/create/",
            json=self.get_payload()
        )
        self.assertEqual(response.status_code, 400, response.json())

    def test_create_product_custom_uom_error(self):
        payload = self.get_payload()
        payload["purchase_uom"] = "kg"
        response = self.test_client.post(
            "/v1/products/create/",
            json=payload
        )
        self.assertEqual(response.status_code, 422, response.json())

    def test_create_product_custom_uom_ok(self):
        payload = self.get_payload()
        payload["purchase_uom"] = "kg"
        payload["purchase_uom_conversion_rate"] = 2.5
        response = self.test_client.post(
            "/v1/products/create/",
            json=payload
        )
        self.assertEqual(response.status_code, 200, response.json())

    def test_create_product_without_variants(self):
        payload = self.get_payload()
        del(payload["variants"])
        response = self.test_client.post(
            "/v1/products/create/",
            json=payload
        )
        self.assertEqual(response.status_code, 200, response.json())

    def test_create_product_without_config_attributes(self):
        payload = self.get_payload()
        del(payload["variants"][0]["config_attributes"])
        response = self.test_client.post(
            "/v1/products/create/",
            json=payload
        )
        self.assertEqual(response.status_code, 200, response.json())

