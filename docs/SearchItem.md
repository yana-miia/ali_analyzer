# SearchItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | AliExpress Product ID  | [optional] 
**title** | **str** | The subject / title of the product  | [optional] 
**category_id** | **int** | The category of the item  | [optional] 
**image_url** | **str** | Image URL for the item  | [optional] 
**detail_url** | **str** | The detail URL of the item  | [optional] 
**lot_size** | **int** | The lot size that the item is sold in  | [optional] 
**lot_unit** | **str** | The unit when describing a lot for this item  | [optional] 
**price** | [**Amount**](Amount.md) |  | [optional] 
**ratings** | **float** | The ratings of this item  | [optional] 
**orders** | **float** | The number of orders of this item  | [optional] 
**freight** | [**SearchItemFreight**](SearchItemFreight.md) |  | [optional] 
**seller** | [**SearchItemSeller**](SearchItemSeller.md) |  | [optional] 
**freight_types** | [**list[SearchItemFreightType]**](SearchItemFreightType.md) | List of freight types available for this item  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


