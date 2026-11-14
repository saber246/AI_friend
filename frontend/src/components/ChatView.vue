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
      >
        <el-menu-item index="1">
          <el-icon><ChatDotRound /></el-icon>
          <template #title>对话</template>
        </el-menu-item>
        <el-menu-item index="2">
          <el-icon><User /></el-icon>
          <template #title>联系人</template>
        </el-menu-item>
        <el-menu-item index="3">
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
        <el-button type="primary" @click="loginDialogVisible = true">登录</el-button>
      </el-header>
      <el-main class="app-main">
        <ChatView />
      </el-main>
    </el-container>
  </el-container>

  <el-dialog
    v-model="loginDialogVisible"
    title="用户登录"
    width="400px"
    center
  >
    <el-form :model="loginForm" :rules="loginRules" ref="loginFormRef">
        <el-form-item label="用户名" prop="username">
            <el-input v-model="loginForm.username" placeholder="请输入用户名"/>
        </el-form-item>
        <el-form-item label="密码" prop="password">
            <el-input v-model="loginForm.password" placeholder="请输入密码"/>
        </el-form-item>
    </el-form>

    <template #footer>
        <el-button type="primary" @click="handleLogin">登录</el-button>
        <el-button @click="loginDialogVisible = false">取消</el-button>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, reactive } from 'vue'
import ChatView from '../views/ChatView.vue'

const isCollapse = ref(true)
const activeMenu = ref('1')
const searchText = ref('')
const loginDialogVisible = ref(false)
const loginFormRef = ref(null)
const loginForm = reactive({
    username: '',
    password: ''
})

const loginRules = reactive({
    username: [
        { required: true, message: '请输入用户名', trigger: 'blur' }
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' }
    ],
})

const handleSearch = () => {
    console.log('hello world')
}

const handleLogin = () => {
    
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
.login-btn {
    margin-left: auto;
}
</style>
