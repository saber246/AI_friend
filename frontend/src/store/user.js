import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/http/api.js'
import { useRouter } from 'vue-router'

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

    async function logout() {
        await api.post('api/user/logout/')
        const router = useRouter()
        id.value = 0
        username.value = ''
        photo.value = ''
        profile.value = ''
        accessToken.value = ''
        router.push('/')
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
