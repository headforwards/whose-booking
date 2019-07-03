# MS Graph Useful Links

Your app registration will need Calendars.Read permission

## Get all room names
https://graph.microsoft.com/beta/me/findRooms

## Get all events for a room (Liskov)
### Using service principal id
https://graph.microsoft.com/beta/users/56a6fc77-23e9-4860-88e8-0f9b2b22deb1/events
### Using room email address
https://graph.microsoft.com/beta/users/opie.liskov@headforwards.com/events 

## Get extended room details
[https://graph.microsoft.com/v1.0/me/people/?$filter=personType/class eq 'Other' and personType/subclass eq 'Room'](https://graph.microsoft.com/v1.0/me/people/?$filter=personType/class eq 'Other' and personType/subclass eq 'Room')

This returns a JSON object with all the room details

```javascript
{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users('8801c8ba-6691-4839-87d3-cfe6bcf5b84d')/people",
    "value": [
        {
            "id": "860b1d31-204a-48c9-99a5-8a31a4e1735b",
            "displayName": "Liskov Meeting Room @ OPIE",
            "givenName": null,
            "surname": null,
            "birthday": "",
            "personNotes": "",
            "isFavorite": false,
            "jobTitle": null,
            "companyName": null,
            "yomiCompany": "",
            "department": null,
            "officeLocation": "2nd floor OPIE far end right hand side by fire escape doors",
            "profession": "",
            "userPrincipalName": "opie.liskov@headforwards.com",
            "imAddress": null,
            "scoredEmailAddresses": [
                {
                    "address": "opie.liskov@headforwards.com",
                    "relevanceScore": 27,
                    "selectionLikelihood": "notSpecified"
                }
            ],
            "phones": [],
            "postalAddresses": [],
            "websites": [],
            "personType": {
                "class": "Other",
                "subclass": "Room"
            }
        }
  }
```

You can also get more information about the room using

[https://graph.microsoft.com/beta/users/{id | userPrincipalName}](https://graph.microsoft.com/beta/users/{id | userPrincipalName})

For example:
https://graph.microsoft.com/beta/users/860b1d31-204a-48c9-99a5-8a31a4e1735b

```javascript

{
    "@odata.context": "https://graph.microsoft.com/beta/$metadata#users/$entity",
    "id": "860b1d31-204a-48c9-99a5-8a31a4e1735b",
    "deletedDateTime": null,
    "accountEnabled": true,
    "ageGroup": null,
    "businessPhones": [],
    "city": null,
    "createdDateTime": "2017-11-23T09:59:13Z",
    "companyName": null,
    "consentProvidedForMinor": null,
    "country": null,
    "department": null,
    "displayName": "Liskov Meeting Room @ OPIE",
    "employeeId": null,
    "faxNumber": null,
    "givenName": null,
    "imAddresses": [],
    "isResourceAccount": null,
    "jobTitle": null,
    "legalAgeGroupClassification": null,
    "mail": "opie.liskov@headforwards.com",
    "mailNickname": "opie.liskov",
    "mobilePhone": null,
    "onPremisesDistinguishedName": null,
    "officeLocation": "2nd floor OPIE far end right hand side by fire escape doors",
    "onPremisesDomainName": null,
    "onPremisesImmutableId": null,
    "onPremisesLastSyncDateTime": null,
    "onPremisesSecurityIdentifier": null,
    "onPremisesSamAccountName": null,
    "onPremisesSyncEnabled": null,
    "onPremisesUserPrincipalName": null,
    "otherMails": [],
    "passwordPolicies": "None",
    "passwordProfile": null,
    "postalCode": null,
    "preferredDataLocation": null,
    "preferredLanguage": null,
    "proxyAddresses": [
        "SMTP:opie.liskov@headforwards.com"
    ],
    "refreshTokensValidFromDateTime": "2017-11-23T09:59:12Z",
    "showInAddressList": null,
    "signInSessionsValidFromDateTime": "2017-11-23T09:59:12Z",
    "state": null,
    "streetAddress": null,
    "surname": null,
    "usageLocation": null,
    "userPrincipalName": "opie.liskov@headforwards.com",
    "externalUserState": null,
    "externalUserStateChangeDateTime": null,
    "userType": "Member",
    "assignedLicenses": [],
    "assignedPlans": [],
    "deviceKeys": [],
    "onPremisesExtensionAttributes": {
        "extensionAttribute1": null,
        "extensionAttribute2": null,
        "extensionAttribute3": null,
        "extensionAttribute4": null,
        "extensionAttribute5": null,
        "extensionAttribute6": null,
        "extensionAttribute7": null,
        "extensionAttribute8": null,
        "extensionAttribute9": null,
        "extensionAttribute10": null,
        "extensionAttribute11": null,
        "extensionAttribute12": null,
        "extensionAttribute13": null,
        "extensionAttribute14": null,
        "extensionAttribute15": null
    },
    "onPremisesProvisioningErrors": [],
    "provisionedPlans": []
}
```

## Get user profile picture

https://graph.microsoft.com/beta/users/opie.liskov@headforwards.com/photo/$value

Try it out at Microsoft [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
