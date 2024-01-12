app = new Vue({
    el:'#heroes_app',
    data: {
        heroes: []
    },
    created: function () {
        const vm = this;
        const GraphQLQuery = `
        query getHero{
          hero(id: 1){
            name
            photo
            link
            owner {
              username
              link
            }
            description
            categories {
              name
              link
            }
            abilities {
              name
              link
              abType {
                mode
              }
              costs {
                cost
                per {
                  unit
                }
                unit {
                  name
                  link
                }
              }
            }
            items {
              name
              link
              itemClass {
                name
                link
              }
              effects {
                name
              }
            }
          }
        }
        `
        axios.get(
            '/graphql/',
            {
                'params': {
                    'query': GraphQLQuery
                },
                'headers': {
                    'Content-Type': 'application/json'
                }
            }
        )
        .then(function (response) {
          vm.heroes = [response.data.data.hero];
        })
    }
})
