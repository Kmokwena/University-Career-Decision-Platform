<script setup>
import { ref, onMounted } from "vue";
const careers = ref([]);

const fetchCareers = async () => {
  try {
    const response = await fetch("/api/career/");
    if (!response.ok && response.status !== 404) {
      throw new Error("Server Error");
    }
    careers.value = await response.json();
  } catch (err) {}
};

onMounted(() => {
  fetchCareers();
});
</script>

<template>
  <div>
    <!-- Show a loading state if Django takes a second -->
    <div v-if="loading">Loading pathways...</div>

    <!-- Show an error if something broke -->
    <div v-else-if="error" style="color: red">Error: {{ error }}</div>

    <!-- Render the raw data to prove the connection works! -->
    <ul v-else>
      <li v-for="career in careers" :key="career.id">
        <strong>{{ career.career_name }}</strong> -
        {{ career.description }}

        <!-- Nested Loop for Qualifications -->
        <ul>
          <li v-for="qual in career.qualification" :key="qual.id">
            🎓 {{ qual.qualification_name }}
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>
