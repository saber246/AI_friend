<script setup>
import { useRoute } from 'vue-router'
const id = useRoute().params.user_id
</script>


<template>
  <div>个人空间: {{id}}</div>
</template>


<style scoped>

</style>



