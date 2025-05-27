import { Component, h, State } from '@stencil/core';
import { fetchSlaData } from '../../snowflake';

interface SlaEntry {
  name: string;
  uptime: number;
}

@Component({
  tag: 'uptime-heatmap',
  styleUrl: 'uptime-heatmap.css',
  shadow: true,
})
export class UptimeHeatmap {
  @State() data: SlaEntry[] = [];
  @State() search: string = '';

  async componentWillLoad() {
    this.data = await fetchSlaData();
  }

  private onInput(ev: Event) {
    const val = (ev.target as HTMLInputElement).value;
    this.search = val;
  }

  private get filtered() {
    return this.data.filter(d => !this.search || d.name.toLowerCase().includes(this.search.toLowerCase()));
  }

  render() {
    return (
      <div>
        <input type="search" onInput={(ev) => this.onInput(ev)} placeholder="Search services" />
        <div class="heatmap">
          {this.filtered.map(item => (
            <div class="row">
              <span class="name">{item.name}</span>
              <span class="cell" style={{backgroundColor: getColor(item.uptime)}}>
                {item.uptime}%
              </span>
            </div>
          ))}
        </div>
      </div>
    );
  }
}

function getColor(uptime: number) {
  if (uptime >= 99.9) return '#2ecc71';
  if (uptime >= 99.0) return '#f1c40f';
  return '#e74c3c';
}
