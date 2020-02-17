<template>
  <b-card
    header="Create your Beat"
    :footer="isUploading ? 'Your Beat is very important to us' : ''"
  >
    <b-alert
      v-model="isFailed"
      variant="danger"
    >
      {{ errorMessage }}
    </b-alert>
    <b-form @submit.prevent="submit">
      <b-form-group>
        <b-form-file
          v-model="file"
          accept="audio/*"
          placeholder="Choose a beatbox audio file..."
          drop-placeholder="Drop beatbox here..."
          :disabled="isUploading"
          required
        />
      </b-form-group>
      <b-button
        type="submit"
        variant="primary"
        :disabled="isUploading"
      >
        <b-spinner
          v-if="isUploading"
          small
        />
        {{ isUploading ? "Processing" : "Submit" }}
      </b-button>
    </b-form>
  </b-card>
</template>

<script>
import axios from 'axios';

const STATUS_INITIAL = 0;
const STATUS_UPLOADING = 1;
const STATUS_SUCCESS = 2;
const STATUS_FAILED = 3;

export default {
  data() {
    return {
      file: undefined,
      status: STATUS_INITIAL,
      errorMessage: '',
    };
  },
  computed: {
    isUploading() { return this.status === STATUS_UPLOADING; },
    isFailed() { return this.status === STATUS_FAILED; },
  },
  mounted() {
    this.status = STATUS_INITIAL;
  },
  methods: {
    async submit() {
      const formData = new FormData();
      formData.append('fileToUpload', this.file);
      this.status = STATUS_UPLOADING;
      try {
        const { data } = await axios.post('/upload', formData);
        this.status = STATUS_SUCCESS;
        this.$emit('done', data);
      } catch (err) {
        this.errorMessage = err;
        this.status = STATUS_FAILED;
      }
    },
  },
};
</script>
