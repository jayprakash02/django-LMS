<template>
  <div>
    <Navbar />
    <div class="container-fluid bg-white text-dark">
      <div class="row">
        <div
          class="order-1 order-md-1 col-12 col-md-2 col-lg-2 py-3 bg-sidebar-light border-right"
        >
          <SecondNav activeTab="Question" />
        </div>
        <div
          class="order-2 order-md-2 col-12 col-md-10 col-lg-10 min-height min-page-height py-3"
        >
          <div class="">
            <div class="d-flex">
              <div class="flex-grow-1"><h1>Question</h1></div>
            </div>
            <div class="min-height">
              <questionCard />
            </div>
            <div class="fixed-bottom bg-light">
              <div class="container-fluid">
                <div class="row">
                  <div class="col-12 col-md-10 ml-auto pb-5 pt-2 bg-light">
                    <form>
                      <div class="form-row align-items-center">
                        <div class="col my-1">
                          <textarea
                            required=""
                            rows="1"
                            name="question"
                            class="form-control false undefined"
                            placeholder="Write a question...."
                          ></textarea
                          ><span></span>
                        </div>
                        <div class="col-auto my-1">
                          <button type="submit" class="btn btn-cfe">
                            Submit
                          </button>
                        </div>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import SecondNav from "@/components/SecondNav.vue";
import questionCard from "@/components/QuestionCard.vue";
export default {
  name: "question",
  components: {
    Navbar,
    SecondNav,
    questionCard,
  },
};
</script>
<style scoped>
.d-block {
  display: block;
}
.bg-sidebar-light {
  background-color: #e9ecef !important;
}
.border-right {
  border-right: 1px solid #dee2e6 !important;
}
.pb-3,
.py-3 {
  padding-bottom: 1rem !important;
}
.pt-3,
.py-3 {
  padding-top: 1rem !important;
}
.btn-cfe {
  background-color: #007cae;
  color: #fff;
}
</style>