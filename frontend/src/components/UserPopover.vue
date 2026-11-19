<template>
    <div style="display: flex; align-items: center" >
        <el-popover placement="bottom" :width="200" trigger="click">
        <template #reference>
            <el-avatar :src="user.photo" />
        </template>
            <div class="user-info" @click="router.push({name: 'space-index', params: {user_id: user.id}})">
                <el-avatar :src="user.photo" :size="50" style="margin-left: 10px" />
                <div class="user-meta">
                    <div class="username">{{ user.username }}</div>
                </div>
            </div>
            <div class="common-button" @click="router.push({name: 'space-index', params: {user_id: user.id}})" style="margin-top: 10px;">
                <home class="icon" />
                <span class="button-text">个人空间</span>
            </div>
            <div class="common-button" @click="router.push({name: 'favorite-index', params: {user_id: user.id}})">
                <yellow_star class="icon" />
                <span class="button-text">我的收藏</span>
            </div>
            <div class="common-button" @click="router.push({name: 'work-index', params: {user_id: user.id}})">
                <work class="icon" />
                <span class="button-text">我的作品</span>
            </div>
            <div class="common-button" @click="router.push({name: 'profile-index'})">
                <edit_profile class="icon" />
                <span class="button-text">编辑资料</span>
            </div>
            <div class="common-button" @click="user.logout">
                <logout class="icon" />
                <span class="button-text">退出登录</span>
          </div>
        </el-popover>
    </div>
</template>


<style scoped>
.user-info {
    display: flex;
}
.username {
    font-size: 15px;
    font-weight: bold;
    margin-left: 20px;
    margin-top: 10px;
}
.common-button {
    display: flex;
    height: 40px;
    align-items: center;
}
.icon {
    width: 30px;
    height: 30px;
    margin-left: 10px;
}
.button-text {
    margin-left: 15px;
    font-size: 17px;
    font-weight: bold;

}


</style>


<script setup>
import { useUserStore } from '@/store/user'
import { useRouter } from 'vue-router'
import yellow_star from './icon/yellow_star.vue';
import logout from './icon/logout.vue'
import work from './icon/work.vue'
import edit_profile from './icon/edit_profile.vue'
import home from './icon/home.vue'

const router = useRouter()
const user = useUserStore()
</script>
