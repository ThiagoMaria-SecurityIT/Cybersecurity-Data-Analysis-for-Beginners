# ⚡ Begginer Friendly Priority Decision Matrix (NIST SP 800-61r2)

| Factor          | Critical          | High               | Medium             | Low                |
|-----------------|-------------------|--------------------|--------------------|--------------------|
| **Account Type**| root/domain admin | service accounts   | guest accounts     | test users         |
| **Impact**      | company-wide      | major systems      | minor systems      | non-production     |
| **Velocity**    | >5 attempts/min   | 2-5 attempts/min   | <2 attempts/min    | single attempt     |
| **Data Risk**   | PII/PCIe          | internal data      | non-sensitive      | none               |

## Examples
- 🔴 **Critical**: 10 root SSH fails in 1min  
- 🟠 **High**: 5 root attempts/2min  
- 🟡 **Medium**: 2 guest FTP fails  
- 🟢 **Low**: 1 failed login to test_db  
