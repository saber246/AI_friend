<template>
  <el-card class="profile-card">
    <span style="padding-top: 10px; font-weight: bold;" shadow: always;>编辑资料</span>

    <div class="avatar-container">
      <el-avatar class="avatar" :src="previewUrl || user.photo" @click="dialogVisible = true" />
      <div class="edit-avatar">点击更换头像</div>
    </div>

    <div class="username">
      <div>用户名</div> 
      <el-input :placeholder=user.username v-model="form.username"></el-input>
    </div>

    <div class="profile-info">
      <div>个人简介</div> 
      <el-input :placeholder=user.profile type="textarea" :rows="4" v-model="form.profile"></el-input>
    </div>

    <div class="btn">
      <el-button class="cancel-btn" @click="handleCancel">取消</el-button>
      <el-button class="save-btn" @click="handleSave">保存</el-button>
    </div>
  </el-card>

  <el-dialog
    title="更换头像"
    v-model="dialogVisible"
    width="70%"
    @opened="initCroppie"
    @closed="destroyCroppie"
  >
    <div ref="cropBox" class="crop-box"></div>
    <input 
      ref='fileInput'
      type='file'
      accept='image/*'
      style='display: none'
      @change='handleFileChange'
    >
    <template #footer>
      <el-button type="primary" @click="pickFile">选择图片</el-button>
      <el-button type="primary" :disabled="!cropSrc" @click="handleCropConfirm">
        确认裁剪
      </el-button>
    </template>
  </el-dialog>
</template>




<style scoped>
.profile-card {
  background-color: rgba(54, 46, 60, 0.999);
  color: white;
  width: 480px;
  margin: 0 auto;
}
.avatar-container {
  align-items: center;
  display: flex;
  flex-direction: column;
}
.avatar {
  margin-top: 20px;
  width: 100px;
  height: 100px;
}
.edit-avatar {
  font-size: 12px;
  color: #ffffff8b;
}
.username {
  margin-top: 20px;
}
.profile-info {
  margin-top: 20px;
}
.btn {
  margin-top: 50px;
}
.cancel-btn {
  margin-left: 10px;
  width: 150px;
  color: white;
  background-color: #ffffff67;
}
.save-btn {
  margin-left: 110px;
  width: 150px;
  color: white;
  background-color: red;
}
.crop-box {
  width: 300px;
  height: 300px;
  margin: 0 auto;
}


</style>


<script setup>
import { ref, reactive } from 'vue'
import Croppie from 'croppie'
import 'croppie/croppie.css'
import { ElMessage } from 'element-plus'
import api, { BASE_URL } from '@/http/api'
import { useUserStore } from '@/store/user'

const user = useUserStore()

// ===== 表单 =====
const form = reactive({
  username: user.username,
  profile: user.profile,
})

// ===== 头像相关状态 =====
const dialogVisible = ref(false)
const fileInput = ref(null)   // 指向隐藏的 <input type="file">
const cropBox = ref(null)     // 指向 Croppie 挂载的 div
const cropSrc = ref('')       // 是否已选图（控制按钮禁用）
const photoFile = ref(null)   // 裁剪后的 File，保存时才上传
const previewUrl = ref('')    // 本地预览 URL
let croppie = null            // Croppie 实例，不需要响应式，用普通变量

// ===== 弹窗打开：初始化 Croppie =====
function initCroppie() {
  if (croppie) return
  croppie = new Croppie(cropBox.value, {
    viewport: { width: 200, height: 200, type: 'circle' }, // 裁剪框：圆形
    boundary: { width: 300, height: 300 },                 // 外层容器
    showZoomer: true,                                      // 显示缩放滑条
  })
}

// ===== 弹窗关闭：销毁实例，释放内存 =====
function destroyCroppie() {
  if (croppie) {
    croppie.destroy()
    croppie = null
  }
  cropSrc.value = ''
}

// ===== 点"选择图片"：代为点击隐藏的 input =====
function pickFile() {
  fileInput.value.click()
}

// ===== 选完文件：校验 → 读成 base64 → 喂给 Croppie =====
function handleFileChange(e) {
  const file = e.target.files[0]
  e.target.value = '' // 清空，否则下次选同一张图不触发 change
  if (!file) return
  if (!file.type.startsWith('image/')) {
    ElMessage.warning('请选择图片文件')
    return
  }
  if (file.size > 5 * 1024 * 1024) {
    ElMessage.warning('图片不能超过 5MB')
    return
  }
  const reader = new FileReader()
  reader.onload = () => {
    cropSrc.value = reader.result
    croppie.bind({ url: reader.result }) // 把图片放进裁剪器
  }
  reader.readAsDataURL(file)
}

// ===== 点"确定裁剪"：拿到裁剪结果 blob =====
async function handleCropConfirm() {
  const blob = await croppie.result({
    type: 'blob',
    size: { width: 300, height: 300 }, // 输出 300x300，够头像用了
    format: 'jpeg',
  })
  // blob 转 File，方便 FormData 上传时带文件名
  photoFile.value = new File([blob], 'avatar.jpg', { type: 'image/jpeg' })
  // 释放上一次的预览 URL，防止内存泄漏
  if (previewUrl.value) URL.revokeObjectURL(previewUrl.value)
  previewUrl.value = URL.createObjectURL(blob)
  dialogVisible.value = false
}

// ===== 保存：FormData 上传 =====
async function handleSave() {
  try {
    const { data } = await api.post('/api/profile/update/', formData)
    if (data.result === '更新成功') {
      // 和登录时同一套写法：拼完整 URL 存进 store
      user.setUserInfo(data, `${BASE_URL}${data.photo}`)
      photoFile.value = null
      if (previewUrl.value) {
        URL.revokeObjectURL(previewUrl.value)
        previewUrl.value = ''
      }
      ElMessage.success('保存成功')
    } else {
      ElMessage.error(data.result || '保存失败')
    }
  } catch {
    ElMessage.error('网络错误，请稍后重试')
  }
}

// ===== 取消：一切恢复到 store 里的状态 =====
function handleCancel() {
  form.username = user.username
  form.profile = user.profile
  photoFile.value = null
  if (previewUrl.value) {
    URL.revokeObjectURL(previewUrl.value)
    previewUrl.value = ''
  }
}


</script>
