# BestSellingSearchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | **str** | The time range to look for best selling products. Can be Top best selling products or Weekly best selling products.  | [optional] [default to 'top']
**category** | **str** | The category to look for best selling products. Only certain categories can be searched for depending on the &#x60;range&#x60;. When range is \&quot;top\&quot;, only the categories [ \&quot;all\&quot;, \&quot;fashion\&quot;, \&quot;electronics\&quot;, \&quot;sports\&quot;, \&quot;health_beauty\&quot;, \&quot;kids_baby\&quot;, \&quot;home_garden\&quot;, \&quot;automotive\&quot; ] are supported. When range is \&quot;weekly\&quot;, only the categories [ \&quot;woman\&quot;, \&quot;men\&quot;, \&quot;electronics\&quot;, \&quot;sports\&quot;, \&quot;health_beauty\&quot;, \&quot;kids_baby\&quot;, \&quot;automotive\&quot; ] are supported.  | [optional] [default to 'electronics']
**skip** | **int** | The number of results to skip. Allows for pagination.  | [optional] [default to 0]
**locale** | **str** | AliExpress locale to use.  | [optional] [default to 'en_US']
**currency** | [**RealtimeCurrency**](RealtimeCurrency.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


