<template>
  <el-card class="login-card">
    <h3 style="text-align: center; margin-top: 10px;">用户登录</h3>
    <el-form 
      :model="loginForm" 
      :rules="loginRules" 
      ref="loginFormRef" 
      label-position="top"
      hide-required-asterisk
      size="large"
    >
      <el-form-item label="用户名" prop="username">
        <el-input v-model="loginForm.username" placeholder="请输入用户名"/>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input v-model="loginForm.password" placeholder="请输入密码"/>
      </el-form-item>
    </el-form>
    <el-button class='login-button' type="primary" @click="handleLogin">登录</el-button>
    <div class="register-link">
      <span style="font-size: 14px;">没有账号，</span>
      <el-link type="primary" @click="router.push({ name: 'register-index' })">
        去注册
      </el-link>
    </div>
  </el-card>
</template>


<style scoped>
.login-card {
  width: 400px;
  margin: 8% auto;
}

.login-button {
  width: 100%;
  margin-top: 10px;
  background-color: black;
}
.register-link {
  text-align: right;
  margin-top: 5px;
}

</style>


<script setup>
import axios from 'axios'
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import api, { BASE_URL } from '@/http/api'
import { ElMessage } from 'element-plus'
import { useUserStore } from '@/store/user'

const userStore = useUserStore()
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

const router = useRouter()
const loading = ref(false)

async function handleLogin() {
  console.log('handleLogin')
  console.log(userStore.photo)
  loginFormRef.value.validate(async valid => {
    if (!valid) return
    loading.value = true
    try {
      const { data } = await api.post('/api/user/login/', loginForm)
      if (data.result === 'success') {
        userStore.setAccessToken(data.access)
        userStore.setUserInfo(data, `${BASE_URL}${data.photo}`)
        ElMessage.success('登录成功')
        router.push({ name: 'home-index' })
      } else {
        ElMessage.error(data.message || '用户名或密码错误')
      }
    } catch {
      ElMessage.error('网络或服务器异常，请稍后再试')
    } finally {
      loading.value = false
    }
  })
  console.log(userStore.photo)
}

</script>