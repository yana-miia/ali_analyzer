# Product

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The AliExpress item ID  | [optional] 
**category_id** | **str** | The item category  | [optional] 
**company_id** | **str** | The company ID  | [optional] 
**seller_id** | **str** | The seller ID  | [optional] 
**title** | **str** | The subject / title of the item  | [optional] 
**status_id** | **int** | The AliExpress status ID  | [optional] 
**status** | **str** | The AliExpress status  | [optional] 
**count_per_lot** | **int** | The number of items per lot  | [optional] 
**wish_list_count** | **int** | Number of times the item has been added to a wishlist  | [optional] 
**unit** | **str** | The unit of the item  | [optional] 
**multi_unit** | **str** | The unit for multiple items  | [optional] 
**seller** | [**ProductSeller**](ProductSeller.md) |  | [optional] 
**reviews** | [**ProductReviews**](ProductReviews.md) |  | [optional] 
**trade** | [**TradeInformation**](TradeInformation.md) |  | [optional] 
**promotion** | [**ProductPromotion**](ProductPromotion.md) |  | [optional] 
**product_images** | **list[str]** | The item images  | [optional] 
**attributes** | [**list[ProductAttribute]**](ProductAttribute.md) | Attributes associated with the AliExpress product  | [optional] 
**html_description** | **str** | The product HTML description  | [optional] 
**price_summary** | [**PriceSummary**](PriceSummary.md) |  | [optional] 
**prices** | [**list[SkuPriceOption]**](SkuPriceOption.md) | All the variations of an AliExpress item and prices associated with each variation  | [optional] 
**shipping** | [**list[ProductShippingOptions]**](ProductShippingOptions.md) | The shipping options of an AliExpress item  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


