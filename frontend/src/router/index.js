import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home-index',
      component: () => import('@/views/homepage/HomepageIndex.vue'),
    },
    {
      path: '/create/',
      name: 'create-index',
      component: () => import('@/views/create/CreateIndex.vue'),
    },
    {
      path: '/friend/',
      name: 'friend-index',
      component: () => import('@/views/friend/FriendIndex.vue'),
    },
    {
      path: '/error/',
      name: 'error-index',
      component: () => import('@/views/error/NotFoundIndex.vue'),
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
    },
    {
      path: '/profile/',
      name: 'profile-index',
      component: () => import('@/views/profile/ProfileIndex.vue'),
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/error/',
      name: 'not-found-index',
    },
    {
      path: '/take/',
      name: 'take-index',
      component: () => import('@/views/take/TakeIndex.vue'),
    },
    {
        path: '/settings/',
        name: 'setting-index',
        component: () => import('@/views/setting/SettingIndex.vue'),
    }
  ],
})

export default router
