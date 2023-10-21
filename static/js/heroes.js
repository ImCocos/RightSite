app = new Vue({
    el:'#heroes_app',
    data: {
        heroes: []
    },
    created: function () {
        const vm = this;
        const queryString = window.location.search;
        axios.get('/api/v1/lores/heroes/' + queryString)
        .then(function (response) {
            vm.heroes = response.data;
        })
    }
})
