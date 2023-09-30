app = new Vue({
    el:'#heroes_app',
    data: {
        heroes: []
    },
    created: function () {
        const vm = this;
        const queryString = window.location.search;
        axios.get('/api/heroes/' + queryString)
        .then(function (response) {
            vm.heroes = response.data;
        })
    }
})
