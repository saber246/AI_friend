<template>
  <el-container class="app-layout">
    <el-aside :width="isCollapse ? '64px' : '200px'" class="app-aside">
      <el-menu
        :default-active="activeMenu"
        :collapse="isCollapse"
        class="app-menu"
        background-color="#304156"
        text-color="#bfcbd9"
        active-text-color="#409eff"
        @select="handleMenuSelect"
      >
        <el-menu-item index="1">
          <el-icon><House /></el-icon>
          <template #title>首页</template>
        </el-menu-item>
        <el-menu-item index="2">
          <el-icon><User /></el-icon>
          <template #title>好友</template>
        </el-menu-item>
        <el-menu-item index="3">
          <el-icon><CirclePlusFilled /></el-icon>
          <template #title>创作</template>
        </el-menu-item>
        <el-menu-item index="4">
          <el-icon><Setting /></el-icon>
          <template #title>设置</template>
        </el-menu-item>
      </el-menu>
    </el-aside>

    <el-container>
      <el-header class="app-header">
        <el-icon class="toggle-btn" @click="isCollapse = !isCollapse">
          <Expand v-if="isCollapse" />
          <Fold v-else />
        </el-icon>
        <span class="navbar-title">Elaina</span>
        <!-- 左边搜索框 -->
        <div class="search-container">
          <el-input
            v-model="searchText"
            placeholder="请输入搜索内容"
            style="width: 450px;"
            @keyup.enter="handleSearch"
            clearable
          />
          <el-button type="primary" size="" @click="handleSearch">
            <el-icon><Search /></el-icon>
            <span>搜索</span>
        </el-button>
        </div>
        <el-button type="info" @click="loginDialogVisible = true">登录</el-button>
      </el-header>
      <el-main class="app-main">
        <slot></slot>
      </el-main>
    </el-container>
  </el-container>

  <el-dialog
    v-model="loginDialogVisible"
    title="用户登录"
    width="360px"
    center
  >
    <el-form :model="loginForm" :rules="loginRules" ref="loginFormRef" label-position="top"hide-required-asterisk>
        <el-form-item label="用户名" prop="username">
            <el-input v-model="loginForm.username" placeholder="请输入用户名"/>
        </el-form-item>
        <el-form-item label="密码" prop="password">
            <el-input v-model="loginForm.password" placeholder="请输入密码"/>
        </el-form-item>
    </el-form>

    <template #footer>
        <el-button class="login-button" @click="handleLogin">登录</el-button>
        <el-button  @click="loginDialogVisible = false">取消</el-button>
        <div style="display: flex; justify-content: flex-end;">没有账号，
            <el-link type="primary" @click="registerDialogVisible = true">去注册</el-link>
        </div>
    </template>
  </el-dialog>

  <el-dialog
    v-model="registerDialogVisible"
    title="用户注册"
    width="400px"
    center
  >
    <el-form 
        :model="registerForm" 
        :rules="registerRules" 
        ref="registerFormRef" 
        label-position="top"
        hide-required-asterisk
        size="large"
    >
        <el-form-item label="用户名" prop="username">
            <el-input v-model="registerForm.username" placeholder="请输入用户名"/>
        </el-form-item>
        <el-form-item label="密码" prop="password">
            <el-input v-model="registerForm.password" placeholder="请输入密码"/>
        </el-form-item>
        <el-form-item label="确认密码" prop="confirmPassword">
            <el-input v-model="registerForm.confirmPassword" placeholder="请确认密码"/>
        </el-form-item>
    </el-form>

    <template #footer>
        <el-button type="primary" @click="handleRegister">注册账户</el-button>
        <el-button  @click="registerDialogVisible = false">取消</el-button>
    </template>
  </el-dialog>
</template>

<script setup>
import { el } from 'element-plus/es/locales.mjs'
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'

const isCollapse = ref(true)
const activeMenu = ref('1')
const searchText = ref('')
const loginDialogVisible = ref(false)
const loginFormRef = ref(null)
const loginForm = reactive({
    username: '',
    password: ''
})
const registerDialogVisible = ref(false)
const registerFormRef = ref(null)
const registerForm = reactive({
    username: '',
    password: '',
    confirmPassword: ''
})
const router = useRouter()

const loginRules = reactive({
    username: [
        { required: true, message: '请输入用户名', trigger: 'blur' }
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' }
    ],
})

const registerRules = reactive({
    username: [
        { required: true, message: '请输入用户名', trigger: 'blur' }
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' }
    ],
    confirmPassword: [
        { required: true, message: '请确认密码', trigger: 'blur' }
    ],
})

const handleSearch = () => {
    console.log('hello world')
}

const handleLogin = () => {
    
}

const handleRegister = () => {

}

const handleMenuSelect = (index) => {
    if (index === '1'){
      router.push({name: 'home-index'})
    }
    else if(index === '2'){
        router.push({name: 'friend-index'})
    }
    else if(index === '3'){
        router.push({name: 'create-index'})
    }
    else if(index === '4'){
        router.push({name: 'setting-index'})
    }
}

</script>

<style scoped>
.app-layout {
  height: 100vh;
}
.app-aside {
  overflow: hidden;
  transition: width 0.28s;
}
.app-menu {
  height: 100%;
  border-right: none;
}
.app-header {
  display: flex;
  align-items: center;
  gap: 12px;
  border-bottom: 1px solid #e4e7ed;
}
.toggle-btn {
  font-size: 20px;
  cursor: pointer;
}
.navbar-title {
  font-size: 16px;
  font-weight: 600;
}
.search-container {
    margin: 0 auto;
    display: flex;
    align-items: center;
    gap: 10px;
}
.login-button {
    background-color: black;
    color: #e4e7ed;
}
</style>


