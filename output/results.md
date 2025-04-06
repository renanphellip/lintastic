## Diagnostics

| Rule | Severity | Context | Messages | Documentations |
| - | - | - | - | - |
| openapi-tags-alphabetical | warn | $ | - "$" should have alphabetical "tags" by name.<br> | - https://www.algum-link-grande.com.br/doc/openapi-tags-alphabetical<br>- https://www.algum-outro-link-grande.com.br/doc/openapi-tags-alphabetical<br> |
| truthy-and-falsy | error | $.info.contact | - $.info.contact.name must not be: empty string, 0, false, null<br> |  |
| truthy-and-falsy | error | $.info.contact | - $.info.contact.url must not be: empty string, 0, false, null<br> |  |
| truthy-and-falsy | error | $.info.contact | - $.info.contact.email must be: empty string, 0, false, null<br> |  |

### Summary

- Total errors: 3
- Total warnings: 1
- Total informations: 0
- Total hints: 0
