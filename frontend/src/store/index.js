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
            sessionStorage.setItem('uid', JSON.stringify(data.uid));
            sessionStorage.setItem('user_name', JSON.stringify(data.user_name));
        }
    },
    actions: {
    },
    getters: {
    },
    modules: {
    }
})