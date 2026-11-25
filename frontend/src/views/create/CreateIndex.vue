<template>
  <div>create-index</div>
  <div v-if="user.accessToken.value === ''">haha</div>
  <div v-else>已经登录</div>
</template>


<style scoped>

</style>


<script setup>
import { useUserStore } from '@/store/user.js'

const user = useUserStore()

</script>
