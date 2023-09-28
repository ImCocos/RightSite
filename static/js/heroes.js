new Vue({
    el:'#all_heroes_app',
    data: {
        heroes: []
    },
    created: function () {
        const vm = this;
        axios.get('/api/heroes/')
        .then(function (response) {
            vm.heroes = response.data;
        })
    }
})
