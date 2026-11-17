import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore('use', () => {
    const id = ref(1)
    const username = ref('eliana')
    const photo = ref('http://192.168.31.171:8000/media/user/photos/default.jpg')
    const profile = ref('111')
    const accesstoken = ref('111')

    function isLogin() {
        return !!accesstoken.value
    }

    function setAccessToken(token) {
        accesstoken.value = token
    }

    function setUserInfo(data) {
        id.value = data.user_id
        username.value = data.username
        photo.value = data.photo
        profile.value = data.profile
    }

    function logout() {
        id.value = 0
        username.value = ''
        photo.value = ''
        profile.value = ''
        accesstoken.value = ''
    }

    return {
        id,
        username,
        photo,
        profile,
        accesstoken,
        isLogin,
        setAccessToken,
        setUserInfo,
        logout,
    }
})
