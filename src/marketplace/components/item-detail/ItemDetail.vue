<template>
  <div v-if="item" class="detail" :grade="item.grade">
    <!-- <button type="button" @click="returnClick">Return</button> -->
    <div class="header">
      <ItemIcon
        :item-id="item.id"
        :item-grade="item.grade"
        :enhancement="item.enhancement"
      />
      <ItemName
        :item-id="item.id"
        :item-name="item.name"
        :item-grade="item.grade"
        :enhancement="item.enhancement"
      />
    </div>
    <div class="info">
      <div class="section">
        <label for="stock">In Stock</label>
        <span id="stock">{{ item.stock }}</span>
      </div>
      <div class="section">
        <label for="base-price">Base Price</label>
        <span id="base-price">{{ item.basePrice }}</span>
      </div>
      <div class="section">
        <label for="total-trades">Total Trades</label>
        <span id="total-trades">{{ item.totalTrades }}</span>
      </div>
      <div class="section">
        <label for="last-sale">Recent Transaction</label>
        <span id="last-sale">{{
          new Date(item.lastSale * 1000).toLocaleString()
        }}</span>
      </div>
    </div>
    <div class="chart">
      <label for="price-chart">Price history</label>
      <Line
        id="price-chart"
        :options="(chartOptions as any)"
        :data="(chartData as any)"
      />
    </div>
    <div class="orders">
      <ItemOrders />
    </div>
  </div>
</template>
<script setup lang="ts">
import { useMarketStore, ViewType } from "@/marketplace/market-store";
import { getPriceHistory } from "@/queries";
import { computed, ref } from "vue";
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
} from "chart.js";
import ItemOrders from "./ItemOrders.vue";
import ItemIcon from "@/components/ItemIcon.vue";
import ItemName from "@/components/ItemName.vue";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
);

const marketStore = useMarketStore();

const item = computed(() => marketStore.selectedEnhancement);

function returnClick() {
  marketStore.viewType = ViewType.ItemList;
}

const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: true,
  scales: {
    y: {
      beginAtZero: false,
    },
  },
  elements: {
    point: {
      radius: 0,
    },
  },
  interaction: {
    mode: "index",
    axis: "x",
    intersect: false,
  },
  tension: 0.2,
  plugins: {
    legend: {
      display: false,
    },
    tooltip: {
      enabled: true,
      backgroundColor: "#fff",
      titleColor: "#000",
      bodyColor: "#000",
      displayColors: false,
      bodyFont: {
        size: 16,
        weight: "bold",
      },
      titleFont: {
        size: 16,
        weight: "normal",
      },
      xAlign: "left",
    },
  },
});

const data = ref<{ x: string; y: number }[]>([]);

if (marketStore.selectedEnhancement) {
  getPriceHistory(
    marketStore.selectedEnhancement.id,
    marketStore.selectedEnhancement.enhancement
  ).then((result) => {
    data.value = [];
    let date = new Date();
    for (let i = 0; i < result.length; i++) {
      data.value.push({
        x: date.toLocaleDateString(),
        y: result[i],
      });
      date = new Date(date.getTime() + 86400000); // + 1 day in ms
    }
  });
}

const chartData = computed(() => ({
  datasets: [{ data: data.value, borderColor: "#9BD0F5" }],
}));
</script>
<style scoped lang="scss">
@import "@/styles/main.scss";

.detail {
  display: grid;
  margin: 0.5rem;

  grid-template:
    "header orders" 1fr
    "info orders" 3fr
    "chart orders" 3fr /
    1fr auto;

  height: 100%;

  .header {
    grid-area: header;

    display: flex;

    flex-direction: row;
    align-items: center;

    padding: 1rem;

    gap: 2rem;
  }

  .orders {
    @include custom-scrollbar;
    grid-area: orders;
    overflow-y: auto;
    overflow-x: hidden;
  }

  .info {
    grid-area: info;

    display: grid;
    grid-template: auto auto / 1fr 1fr;

    justify-self: center;
    align-self: center;

    gap: 1.5rem;

    padding: 2rem 3em;
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    border-top: 1px solid rgba(255, 255, 255, 0.2);

    .section {
      display: flex;
      flex-direction: column;

      padding: 0.25rem;

      border: 1px solid rgb(56, 56, 56);
      border-radius: 8px;

      background-color: #2b2b2b;
      box-shadow: 4px 4px 24px 0px rgba(0, 0, 0, 0.75);

      align-content: space-between;
      align-items: center;

      label {
        padding: 0.25rem;
        font-size: 80%;
        color: rgba(196, 196, 196, 0.75);
      }

      span {
        font-size: 120%;
        padding: 0.5rem;
      }
    }
  }

  .chart {
    grid-area: chart;

    label {
      font-size: 80%;
      color: rgba(196, 196, 196, 0.75);
    }
  }
}
</style>
