import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/store/user.js'
import { ElMessage } from 'element-plus'
import api, { BASE_URL } from '@/http/api.js'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home-index',
      component: () => import('@/views/homepage/HomepageIndex.vue'),
      meta: {
        needLogin: false
      }
    },
    {
      path: '/create/',
      name: 'create-index',
      component: () => import('@/views/create/CreateIndex.vue'),
      meta: {
        needLogin: true
      }
    },
    {
      path: '/friend/',
      name: 'friend-index',
      component: () => import('@/views/friend/FriendIndex.vue'),
      meta: {
        needLogin: true
      }
    },
    {
      path: '/user/account/login/',
      name: 'login-index',
      component: () => import('@/views/user/account/LoginIndex.vue'),

    },
    {
      path: '/user/account/register/',
      name: 'register-index',
      component: () => import('@/views/user/account/RegisterIndex.vue'),
    },
    {
      path: '/user/space/:user_id/',
      name: 'space-index',
      component: () => import('@/views/user/space/SpaceIndex.vue'),
      meta: {
        needLogin: false
      }
    },
    {
        path: '/user/space/:user_id/favorite/',
        name: 'favorite-index',
        component: () => import('@/views/user/space/favorite/FavoriteIndex.vue'),
        meta: {
        needLogin: true
      }
    },
    {
      path: '/profile/',
      name: 'profile-index',
      component: () => import('@/views/profile/ProfileIndex.vue'),
      meta: {
        needLogin: true
      }
    },
    {
        path: '/settings/',
        name: 'setting-index',
        component: () => import('@/views/setting/SettingIndex.vue'),
        meta: {
        needLogin: false
      }
    },
    {
      path: '/error/',
      name: 'error-index',
      component: () => import('@/views/error/NotFoundIndex.vue'),
      meta: {
        needLogin: false
      }
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/error/',
      name: 'not-found-index',
      meta: {
        needLogin: false
      }
    },
  ],
})

router.beforeEach( async (to) => {
    const user = useUserStore()
    if (user.isLogin()) return true
    try {
        const { data } = await api.post('api/user/refresh/')
        if(data.result === 'success') {
            user.setAccessToken(data.access)
            user.setUserInfo(data, `${BASE_URL}${data.photo}`)
            return true
        } else {
            ElMessage.error(data.message)
        } 
    } catch (error) {
        
    }

    if(to.meta.needLogin) {
        ElMessage.error('没有权限，请登录')
        return '/user/account/login/'
    }
    return true

})

export default router
