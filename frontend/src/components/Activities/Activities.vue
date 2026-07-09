<template>
  <div class="activities-placeholder border rounded-md">
    <p class="text-gray-500 p-4">Activity timeline will appear here.</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const emailBox = ref({ show: false })
const all_activities = ref({ reload: () => {} })

function changeTabTo(tab) {
  console.log('Tab changed to', tab)
}

defineExpose({
  emailBox,
  all_activities,
  changeTabTo
})
</script>
