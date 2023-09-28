new Vue({
    el:'#all_stories_app',
    data: {
        stories: []
    },
    created: function () {
        const vm = this;
        axios.get('/api/stories/')
        .then(function (response) {
            vm.stories = response.data;
        })
    }
})
