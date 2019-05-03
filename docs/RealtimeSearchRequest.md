# RealtimeSearchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **int** | The category to filter by  | [optional] 
**text** | **str** | The text to filter by  | [optional] 
**price_range** | [**DoubleRange**](DoubleRange.md) |  | [optional] 
**ship_to_country** | **str** | The 2 character ISO code of the country where the item will be shipped to  | [optional] 
**ship_from_country** | **str** | The 2 character ISO code of the country where the item is shipped from  | [optional] 
**sort** | **str** | The sort order of the result  | [optional] [default to 'BEST_MATCH']
**skip** | **int** | Number of items to skip, used for pagination  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


