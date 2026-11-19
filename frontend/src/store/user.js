import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore('use', () => {
    const id = ref()
    const username = ref('')
    const photo = ref('http://192.168.31.171:8000/media/user/photos/default.jpg')
    const profile = ref('')
    const accessToken = ref('')  

    function isLogin() {
        return !!accessToken.value
    }

    function setAccessToken(token) {
        accessToken.value = token
    }

    function setUserInfo(data, photoUrl) {
        id.value = data.user_id
        username.value = data.username
        photo.value = photoUrl
        profile.value = data.profile
    }

    function logout() {
        id.value = 0
        username.value = ''
        photo.value = ''
        profile.value = ''
        accessToken.value = ''
    }


    return {
        id,
        username,
        photo,
        profile,
        accessToken,
        isLogin,
        setAccessToken,
        setUserInfo,
        logout,
    }
})
