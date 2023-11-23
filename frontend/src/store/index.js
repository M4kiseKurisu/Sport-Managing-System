// vuex 仓库
import { createStore } from 'vuex'

export default createStore({
    state: {
        uid: null,
        user_name: null
    },
    mutations: {
        userLogin(state, data) {
            state.uid = data.uid
            state.user_name = data.user_name
            state.picture = data.picture ? 'http://127.0.0.1:8000' + data.picture : './src/images/emptyAvatar.png'
            console.log(state.picture)
            sessionStorage.setItem('uid', JSON.stringify(data.uid));
            sessionStorage.setItem('user_name', JSON.stringify(data.user_name));
            sessionStorage.setItem('picture', state.picture);
        }
    },
    actions: {
    },
    getters: {
    },
    modules: {
    }
})