<template>
  <el-card class="register-card">
    <h3 style="text-align: center; margin-top: 10px;">用户注册</h3>
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
      <el-form-item label="密码" prop="password1">
        <el-input v-model="registerForm.password1" placeholder="请输入密码"/>
      </el-form-item>
      <el-form-item label="确认密码" prop="password2">
        <el-input v-model="registerForm.password2" placeholder="请确认密码"/>
      </el-form-item>
    </el-form>
    <el-button class='register-button' type="primary" @click="handleRegister">注册</el-button>
    <div class="register-link">
      <span style="font-size: 14px;">已有账号，</span>
      <el-link type="primary" @click="router.push({ name: 'login-index' })">
        去登录
      </el-link>
    </div>
  </el-card>
</template>


<style scoped>
.register-card {
  width: 400px;
  margin: 8% auto;
}

.register-button {
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
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import api, { BASE_URL } from '@/http/api'
import { ElMessage } from 'element-plus'
import { useUserStore } from '@/store/user'

const userStore = useUserStore()
const registerFormRef = ref(null)
const registerForm = reactive({
    username: '',
    password1: '',
    password2: ''
})
const registerRules = reactive({
    username: [
        { required: true, message: '请输入用户名', trigger: 'blur' }
    ],
    password1: [
        { required: true, message: '请输入密码', trigger: 'blur' }
    ],
    password2: [
        { required: true, message: '请输入密码', trigger: 'blur' }
    ],
})

const router = useRouter()

async function handleRegister() {
  registerFormRef.value.validate(async valid => {
    if(!valid) return
    if(registerForm.password1 !== registerForm.password2){
      ElMessage.error('两次密码不一致')
      return
    }
    try{
      const { data } = await api.post('/api/user/register/', registerForm)
      if(data.result === 'success'){
        ElMessage.success('注册成功')
        userStore.setAccessToken(data.access)
        userStore.setUserInfo(data, `${BASE_URL}${data.photo}`)
        router.push({ name: 'home-index' })
      } else {
        ElMessage.error(data.message || '注册失败')
      }
    } catch {
      ElMessage.error('网络或服务器异常，请稍后再试')
    } 
  })
    
}

</script>
