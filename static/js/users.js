new Vue({
    el:'#all_users_app',
    data: {
        users: []
    },
    created: function () {
        const vm = this;
        axios.get('/api/v1/users/')
        .then(function (response) {
            vm.users = response.data;
        })
    }
})
