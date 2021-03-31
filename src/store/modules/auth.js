import api from '../../services/api'

const state = {
    key: null,
    pk: null,
    username: null,
    email: null,
    first_name: null,
    last_name: null,
}
const getters = {
    loggedIn(state) {
        return state.key != null
    }
}
const actions = {
    userLogout(context) {
        if (context.getters.loggedIn) {
            context.commit('destroyToken')
        }
    },
    userLogin(context, usercredentials) {
        return new Promise((resolve, reject) => {
            api.post('rest-auth/login/', {
                username: usercredentials.username,
                password: usercredentials.password
            })
                .then(response => {
                    context.commit('updateStorage', { key: response.data.key })
                    resolve()
                })
                .catch(err => {
                    reject(err)
                })
        })
    },
    getCredential(context) {
        return new Promise((resolve, reject) => {
            return api.get('rest-auth/user/')
                .then(response => {
                    context.commit('updateCredential', { pk: response.data.pk, username: response.data.username, first_name: response.data.first_name, last_name: response.data.last_name, email: response.data.email })
                    resolve()
                })
                .catch(err =>{
                    reject(err)
                })

        })
    }
}
const mutations = {
    updateStorage(state, { key }) {
        state.key = key
    },
    updateCredential(state, { pk,username,first_name,last_name,email }) {
        state.pk = pk
        state.username = username
        state.first_name = first_name
        state.last_name = last_name
        state.email = email
    },
    destroyToken(state) {
        state.key = null
        state.pk = null
        state.username = null
        state.first_name = null
        state.last_name = null
        state.email = null
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}